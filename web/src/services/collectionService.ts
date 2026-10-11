import { requete } from './httpClient';

export const getCollection = async () => {
  return await requete('/me/collection');
};

export const addGameToCollection = async (gameId: number) => {
  return await requete(`/me/collection?item_id=${gameId}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      item_id: gameId,
      statut: "a_decouvrir"
    })
  });
};

export const addGameToGroup = addGameToCollection;

export const updateCollectionEntry = async (entryId: number, data: { statut?: string, note?: number | null, commentaire?: string | null }) => {
  return await requete(`/me/collection/${entryId}`, {
    method: 'PATCH',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  });
};

export const getCollectionStats = async () => {
  return await requete('/me/collection/stats');
};
