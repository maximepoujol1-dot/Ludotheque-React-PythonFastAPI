import React from 'react'
import CatalogueCard from './CatalogueCard'
import type { Game } from '../types/type'

export interface GameListResponse {
  total: number
  page: number
  limit: number
  results: Game[]
}

const CatalogueList = ({ results }: GameListResponse) => {
  if (results.length === 0) {
    return <p>Aucun jeu</p>
  }

  return (
    <ul className="m-0 grid list-none grid-cols-1 gap-6 p-0 sm:grid-cols-2 xl:grid-cols-3">
      {results.map((game) => (
        <li key={game.id} className="min-w-0">
          <CatalogueCard game={game} />
        </li>
      ))}
    </ul>
  )
}

export default CatalogueList
