import React from 'react'
import { useState, useEffect } from 'react'
import CatalogueList from "../components/CatalogueList"
import { getItems } from '../services/itemService'

const HomePage = () => {
  const [games, setGames] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [page, setPage] = useState(1)
  const [filter, setFilter] = useState<string | null>(null);
  const [total, setTotal] = useState(0)
  const limit = 12

  useEffect(() => {
    setLoading(true)
    getItems(page,filter)
      .then(data => {
        setGames(data.results || data)
        setTotal(data.total || 0)
        setLoading(false)
      })
      .catch(() => {
        setError("Impossible de charger les jeux")
        setLoading(false)
      })
  }, [page,filter])

  if (loading) {
    return <div className="p-8">Chargement en cours...</div>
  }

  if (error) {
    return <div className="p-8 text-red-600 font-bold">{error}</div>
  }

  const totalPages = Math.ceil(total / limit) || 1

  return (
    <div className="p-8">

      <div className='gap-4'> 
          <button className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300" onClick={()=>setFilter("fps")}> FPS </button>
          <button className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300" onClick={()=>setFilter("rpg")}> RPG </button>
          <button className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300" onClick={()=>setFilter("rts")}> RTS </button>
          <button className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300" onClick={()=>setFilter("gestion")}> GESTION</button>
          <button className="bg-green-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300" onClick={()=>setFilter(null)}> RESET</button>
      </div>
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
