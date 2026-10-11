import React, { useEffect, useState } from 'react';
import { getCollection } from '../services/collectionService';
import CollectionList from '../components/CollectionList';
import { useCollection } from '../contexts/collectionContext';

const CollectionPage = () => {
  const { collection, setCollection } = useCollection();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCollection = async () => {
      try {
        const data = await getCollection();
        setCollection(data.results || data || []);
      } catch (err) {
        console.error("Erreur de récupération de la collection :", err);
        setError("Impossible de charger votre collection.");
      } finally {
        setLoading(false);
      }
    };

    fetchCollection();
  }, []);

  if (loading) {
    return <div className="p-8 text-white font-semibold">Chargement de votre collection...</div>;
  }

  if (error) {
    return <div className="p-8 text-red-500 font-bold">{error}</div>;
  }

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-8">Ma Collection</h1>
      <CollectionList games={collection} />
    </div>
  );
};

export default CollectionPage;
