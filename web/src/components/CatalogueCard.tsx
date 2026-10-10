import React from 'react'
import Card from './Card'
import type { Game } from '../types/type'

interface Props {
  game: Game
}

const CatalogueCard = ({ game }: Props) => {
  return (
    <Card
      title={game.titre}
      style="relative flex h-full w-full flex-col overflow-hidden bg-white shadow-xl border border-gray-200 border-t-4 border-t-green-500 rounded-2xl dark:bg-dark-surface dark:border-white/10 [&>h1]:px-6 [&>h1]:pr-28 [&>h1]:pt-6 [&>h1]:text-xl [&>h1]:font-bold [&>h1]:text-gray-900 dark:[&>h1]:text-white"
    >
      <div className="flex flex-1 flex-col px-6 pb-6">
        <span className="absolute right-6 top-5 z-10 w-fit rounded-full bg-green-50 px-3 py-1 text-sm font-semibold capitalize text-green-700 dark:bg-green-500/10 dark:text-green-400">
          {game.categorie}
        </span>
        {game.image_url && (
          <img
            src={game.image_url}
            alt={`Illustration de ${game.titre}`}
            className="mb-5 aspect-[16/9] w-full rounded-lg object-cover"
          />
        )}

        <p className="mb-5 flex-1 leading-relaxed text-gray-600 dark:text-gray-300">
          {game.description || 'Aucune description disponible.'}
        </p>
        <dl className="mb-6 grid grid-cols-2 gap-x-4 gap-y-3 border-t border-gray-200 pt-4 text-sm dark:border-white/10">
          <div>
            <dt className="font-medium text-gray-500 dark:text-gray-400">Année</dt>
            <dd className="mt-1 text-gray-900 dark:text-white">{game.annee}</dd>
          </div>
          <div>
            <dt className="font-medium text-gray-500 dark:text-gray-400">Studio</dt>
            <dd className="mt-1 text-gray-900 dark:text-white">{game.studio}</dd>
          </div>
          <div className="col-span-2">
            <dt className="font-medium text-gray-500 dark:text-gray-400">Direction</dt>
            <dd className="mt-1 text-gray-900 dark:text-white">{game.directeur}</dd>
          </div>
        </dl>
        <button className="mt-auto w-full cursor-pointer rounded-lg bg-green-500 px-4 py-2 font-semibold text-white shadow-md transition hover:bg-green-600 active:scale-[0.98]" onClick={() => alert("Tu as cliqué sur le jeu numéro " + game.id)}>
          Ajouter à ma collection
        </button>
      </div>
    </Card>
  )
}

export default CatalogueCard
