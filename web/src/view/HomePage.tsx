import React from 'react'
import { useState, useEffect } from 'react'
import CatalogueList from "../components/CatalogueList"
import { getItems } from '../services/itemService'

const HomePage = () => {
  const [games, setGames] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [page, setPage] = useState(1)
  const [total, setTotal] = useState(0)
  const limit = 12

  useEffect(() => {
    setLoading(true)
    getItems(page)
      .then(data => {
        setGames(data.results || data)
        setTotal(data.total || 0)
        setLoading(false)
      })
      .catch(() => {
        setError("Impossible de charger les jeux")
        setLoading(false)
      })
  }, [page])

  if (loading) {
    return <div className="p-8">Chargement en cours...</div>
  }

  if (error) {
    return <div className="p-8 text-red-600 font-bold">{error}</div>
  }

  const totalPages = Math.ceil(total / limit) || 1

  return (
    <div className="p-8">
      <CatalogueList total={total} page={page} limit={limit} results={games} />

      <div className="flex gap-4 mt-4">
        <button
          disabled={page === 1}
          className="bg-blue-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300"
          onClick={() => setPage(page - 1)}
        >
          Précédent
        </button>

        <span className="py-2">Page {page} sur {totalPages}</span>

        <button
          disabled={page >= totalPages}
          className="bg-blue-500 text-white font-bold py-2 px-4 rounded disabled:bg-gray-300"
          onClick={() => setPage(page + 1)}
        >
          Suivant
        </button>
      </div>
    </div>
  )
}

export default HomePage
