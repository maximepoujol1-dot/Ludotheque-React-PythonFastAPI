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
    <ul className="flex flex-wrap list-none p-0 m-0">
      {results.map((game) => (
        <li key={game.id}>
          <CatalogueCard game={game} />
        </li>
      ))}
    </ul>
  )
}

export default CatalogueList
