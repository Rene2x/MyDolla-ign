function Header() {
  return (
    <header className="bg-slate-900/80 border-b border-slate-700 sticky top-0 z-10">
      <div className="container mx-auto px-4 py-3 max-w-2xl flex items-center justify-between">
        <a href="#" className="text-lg font-semibold text-white no-underline">
          My Dolla $ign
        </a>
        <a
          href="#budget"
          className="text-sm text-emerald-300 hover:text-emerald-200 no-underline"
        >
          Budget form
        </a>
      </div>
    </header>
  )
}

export default Header
