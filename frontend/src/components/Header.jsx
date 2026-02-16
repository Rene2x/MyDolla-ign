/**
 * ============================================
 * ASSIGNED TO: Member 1 (Frontend Lead)
 * 
 * Header component with navigation.
 * TODO:
 * 1. Add navigation links if needed
 * 2. Make it responsive for mobile
 * 3. Add any branding elements
 * ============================================
 */

function Header() {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-4 py-4 max-w-4xl">
        <div className="flex items-center justify-between">
          {/* Logo / Brand */}
          <div className="flex items-center space-x-2">
            <span className="text-3xl font-bold text-green-600">$</span>
            <h1 className="text-2xl font-bold text-green-600">
              My Dolla $ign
            </h1>
          </div>
          
          {/* Navigation - TODO: Add more links as needed */}
          <nav className="hidden md:flex space-x-6">
            <a 
              href="#budget" 
              className="text-gray-600 hover:text-green-600 transition-colors"
            >
              Budget Tool
            </a>
            <a 
              href="#glossary" 
              className="text-gray-600 hover:text-green-600 transition-colors"
            >
              Learn
            </a>
          </nav>
        </div>
      </div>
    </header>
  )
}

export default Header
