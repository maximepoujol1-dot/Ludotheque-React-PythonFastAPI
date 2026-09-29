import React from 'react'
import type { Game } from '../types/type'

interface Props {
  game: Game
}

const CatalogueCard = ({ game }: Props) => {
  return (
    <div className="border-2 border-gray-300 rounded-lg p-4 m-4 w-72 bg-white shadow-sm flex flex-col">
      <h2 className="text-xl font-bold mb-2 text-black">{game.titre}</h2>
      <p className="text-gray-600 mb-4 flex-grow">{game.description}</p>

      <button
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded w-full mt-auto"
        onClick={() => alert("Tu as cliqué sur le jeu numéro " + game.id)}
      >
        add
      </button>
    </div>
  )
}

export default CatalogueCard
