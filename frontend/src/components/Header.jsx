function Header() {
  return (
    <header className="bg-white/90 backdrop-blur-sm border-b border-slate-200/80 sticky top-0 z-10">
      <div className="container mx-auto px-4 py-3 max-w-4xl">
        <div className="flex items-center justify-between">
          <a href="#" className="flex items-center gap-2 no-underline">
            <span className="text-2xl font-bold bg-gradient-to-r from-emerald-600 to-teal-600 bg-clip-text text-transparent">
              My Dolla $ign
            </span>
            <span className="text-slate-400 text-lg">$</span>
          </a>
          <nav className="flex items-center gap-4">
            <a
              href="#budget"
              className="text-slate-600 hover:text-emerald-600 font-medium text-sm transition-colors"
            >
              Budget Tool
            </a>
          </nav>
        </div>
      </div>
    </header>
  )
}

export default Header
