import React, { useEffect, useState } from 'react';
import Card from '../components/Card';
import { getCollectionStats } from '../services/collectionService';

const StatPage = () => {
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const data = await getCollectionStats();
        setStats(data);
      } catch (err) {
        console.error("Error fetching statistics:", err);
        setError("Failed to load statistics.");
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  if (loading) {
    return <div className="p-8 text-white font-semibold">Loading statistics...</div>;
  }

  if (error) {
    return <div className="p-8 text-red-500 font-bold">{error}</div>;
  }

  const total = stats?.total ?? 0;
  const parStatut = stats?.par_statut || {};
  const aDecouvrir = parStatut.a_decouvrir ?? 0;
  const enCours = parStatut.en_cours ?? 0;
  const termine = parStatut.termine ?? parStatut.termines ?? 0;

  return (
    <div className="p-8 max-w-5xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-900 dark:text-white mb-8">Collection Statistics</h1>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <Card title="Total Games" style="p-6 bg-white shadow-xl border border-gray-200 border-t-4 border-t-blue-500 rounded-2xl dark:bg-dark-surface dark:border-white/10">
          <p className="text-4xl font-extrabold text-blue-500 mt-2">{total}</p>
        </Card>

        <Card title="To Discover" style="p-6 bg-white shadow-xl border border-gray-200 border-t-4 border-t-yellow-500 rounded-2xl dark:bg-dark-surface dark:border-white/10">
          <p className="text-4xl font-extrabold text-yellow-500 mt-2">{aDecouvrir}</p>
        </Card>

        <Card title="In Progress" style="p-6 bg-white shadow-xl border border-gray-200 border-t-4 border-t-green-500 rounded-2xl dark:bg-dark-surface dark:border-white/10">
          <p className="text-4xl font-extrabold text-green-500 mt-2">{enCours}</p>
        </Card>

        <Card title="Completed" style="p-6 bg-white shadow-xl border border-gray-200 border-t-4 border-t-purple-500 rounded-2xl dark:bg-dark-surface dark:border-white/10">
          <p className="text-4xl font-extrabold text-purple-500 mt-2">{termine}</p>
        </Card>
      </div>
    </div>
  );
};

export default StatPage;
