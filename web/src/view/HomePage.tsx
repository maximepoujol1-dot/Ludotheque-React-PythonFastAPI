import React from 'react'
import { useState, useEffect } from 'react'
import CatalogueList from "../components/CatalogueList"
import { getItems } from '../services/itemService'
import Card from '../components/Card'

const HomePage = () => {
  const [name, setName] = useState<string | null>(null)
  const [debouncedName, setDebouncedName] = useState(name)
  const [games, setGames] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [page, setPage] = useState(1)
  const [filter, setFilter] = useState<string | null>(null);
  const [total, setTotal] = useState(0)
  const limit = 12
  
  const totalReset = () => {
    setFilter(null)
    setName(null)
  }

  useEffect(() => {
    const timer = window.setTimeout(() => {setDebouncedName(name)}, 400)
    return () => window.clearTimeout(timer)
  }, [name])


  useEffect(() => {
    setLoading(true)
    getItems(debouncedName, page,filter)
      .then(data => {
        setGames(data.results || data)
        setTotal(data.total || 0)
        setLoading(false)
      })
      .catch(() => {
        setError("Impossible de charger les jeux")
        setLoading(false)
      })
  }, [debouncedName,page,filter])

  if (loading) {
    return <div className="p-8">Chargement en cours...</div>
  }

  if (error) {
    return <div className="p-8 text-red-600 font-bold">{error}</div>
  }

  const totalPages = Math.ceil(total / limit) || 1

  return (
    <div className="p-8">

      <Card title={""} style={'flex flex-row flex-wrap items-center gap-3 w-full max-w-none p-5 sm:p-6 card bg-white dark:bg-dark-surface shadow-xl border border-gray-200 dark:border-white/10 border-t-4 border-t-green-500 rounded-2xl'} > 
          <input id="game-search"
          className="w-auto min-w-[200px] flex-1 rounded-xl border border-gray-300 bg-gray-50 px-4 py-3 text-gray-900 placeholder:text-gray-400 transition focus:border-green-500 focus:bg-white focus:outline-none focus:ring-2 focus:ring-green-200 dark:border-white/10 dark:bg-white/5 dark:text-white dark:placeholder:text-gray-500 dark:focus:bg-white/10 dark:focus:ring-green-500/30 sm:max-w-md"
          type="search"
          value={name ?? ''}
          onChange={(e) => {setName(e.target.value || null)
            setPage(1)
          }}
          placeholder="Search games..."
        />
          <button className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300 transition hover:bg-green-600" onClick={()=>setFilter("fps")}> FPS </button>
          <button className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300 transition hover:bg-green-600" onClick={()=>setFilter("rpg")}> RPG </button>
          <button className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300 transition hover:bg-green-600" onClick={()=>setFilter("rts")}> RTS </button>
          <button className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300 transition hover:bg-green-600" onClick={()=>setFilter("gestion")}> GESTION</button>
          <button className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300 transition hover:bg-green-600" onClick={()=>totalReset()}> RESET</button>
        </Card>
          
      <br/>
      <CatalogueList total={total} page={page} limit={limit} results={games} />

      <div className="flex gap-4 mt-4">
        <button
          disabled={page === 1}
          className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300"
          onClick={() => setPage(page - 1)}
        >
          Précédent
        </button>

        <span className="py-2">Page {page} sur {totalPages}</span>

        <button
          disabled={page >= totalPages}
          className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300"
          onClick={() => setPage(page + 1)}
        >
          Suivant
        </button>
      </div>
    </div>
  )
}

export default HomePage
