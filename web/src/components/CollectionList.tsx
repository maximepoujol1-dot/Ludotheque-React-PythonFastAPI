import React from 'react';
import type { CollectionEntry } from '../contexts/collectionContext';
import CollectionCard from './CollectionCard';

interface CollectionListProps {
  games: CollectionEntry[];
}

const CollectionList = ({ games }: CollectionListProps) => {
  if (!Array.isArray(games)) {
    return (
      <div className="p-4 bg-red-100/10 border border-red-500 rounded-lg">
        <p className="text-red-500 font-bold">Votre session a expiré ou les données sont invalides.</p>
        <p className="text-gray-400 text-sm">Veuillez vous reconnecter pour voir votre collection.</p>
      </div>
    );
  }

  if (games.length === 0) {
    return <p className="text-gray-600 dark:text-gray-400">Votre collection est vide. Allez sur l'accueil pour ajouter des jeux !</p>;
  }

  return (
    <ul className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
      {games.map((entry, index) => (
        <li key={entry.id || index} className="h-full">
          <CollectionCard entry={entry} />
        </li>
      ))}
    </ul>
  );
};

export default CollectionList;
