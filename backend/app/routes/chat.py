"""
Chat API routes - simple budgeting chatbot powered by Gemini.
"""

from flask import Blueprint, request, jsonify

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/chat', methods=['POST'])
def chat():
  """
  Simple budgeting chatbot endpoint.

  Expected JSON body:
  {
      "message": "How can I cut my food spending?",
      "context": {
          "monthly_income": 3000,
          "goal": "emergency_fund"
      }
  }
  """
  from app.services.ai_service import get_gemini_client, GEMINI_AVAILABLE

  if not GEMINI_AVAILABLE:
      return jsonify({
          'error': 'unavailable',
          'message': 'Chatbot is currently unavailable.'
      }), 503

  data = request.get_json() or {}
  message = (data.get('message') or '').strip()
  context = data.get('context') or {}

  if not message:
      return jsonify({
          'error': 'invalid_request',
          'message': 'message is required'
      }), 400

  monthly_income = context.get('monthly_income')
  goal = context.get('goal')

  context_lines = []
  if monthly_income is not None:
      context_lines.append(f"- Monthly income: ${monthly_income}")
  if goal:
      context_lines.append(f"- Goal: {goal}")

  context_text = "\n".join(context_lines) if context_lines else "No additional context."

  try:
      client = get_gemini_client()

      prompt = f"""User question:
{message}

User context:
{context_text}

Answer in 3-6 short sentences. Use simple language. Focus on practical budgeting and saving steps."""

      response = client.models.generate_content(
          model="gemini-2.0-flash",
          contents=prompt,
          config={
              "max_output_tokens": 400,
              "temperature": 0.6,
          },
      )
      text = response.text or ''

      return jsonify({
          'reply': text.strip(),
      }), 200

  except Exception as e:
      # When Gemini quota is exhausted or any other error occurs, fall back to a simple rule-based reply
      print(f"Chatbot error (falling back to rule-based reply): {e}")

      fallback = [
          "I’m having trouble reaching the AI service right now, ",
          "so here’s a general budgeting suggestion instead.\n\n",
      ]
      if monthly_income:
          fallback.append(
              f"Based on a monthly income of ${monthly_income}, start by aiming to save 10–20% each month if you can. "
          )
      fallback.append(
          "Pick one or two categories to focus on (like food or entertainment), track what you actually spend for a month, "
          "and then set a small, realistic reduction goal for next month (for example, $25–$50 less). "
          "Automating a transfer to savings on payday is one of the easiest ways to make progress without having to think about it every time."
      )

      return jsonify({
          'reply': "".join(fallback),
      }), 200

