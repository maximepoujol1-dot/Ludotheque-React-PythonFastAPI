import React, { useState } from 'react';
import Card from './Card';
import type { CollectionEntry } from '../contexts/collectionContext';
import { useCollection } from '../contexts/collectionContext';
import { updateCollectionEntry } from '../services/collectionService';

const inputStyle = "w-full bg-gray-50 dark:bg-white/5 text-gray-900 dark:text-white border border-gray-300 dark:border-white/10 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-green-500 focus:ring-1 focus:ring-green-500 mb-3";

export default function CollectionCard({ entry }: { entry: CollectionEntry }) {
  const itemInfo = entry.item;
  const { updateEntry } = useCollection();
  const [isEditing, setIsEditing] = useState(false);
  const [editStatut, setEditStatut] = useState(entry.statut);
  const [editNote, setEditNote] = useState<number | string>(entry.note ?? '');
  const [editCommentaire, setEditCommentaire] = useState(entry.commentaire ?? '');
  const [isSaving, setIsSaving] = useState(false);

  if (!itemInfo) return <div className="text-red-500">Erreur : données introuvables</div>;

  const handleSave = async () => {
    setIsSaving(true);
    try {
      const payload = { statut: editStatut, note: editNote === '' ? null : Number(editNote), commentaire: editCommentaire === '' ? null : editCommentaire };
      const updatedEntry = await updateCollectionEntry(entry.id, payload);
      updateEntry(entry.id, updatedEntry);
      setIsEditing(false);
    } catch (err) { alert("Impossible de sauvegarder les modifications."); }
    finally { setIsSaving(false); }
  };

  return (
    <Card title={itemInfo.titre || 'Jeu sans titre'} style="relative flex h-full w-full flex-col overflow-hidden bg-white shadow-xl border border-gray-200 border-t-4 border-t-green-500 rounded-2xl dark:bg-dark-surface dark:border-white/10 [&>h1]:px-6 [&>h1]:pr-28 [&>h1]:pt-6 [&>h1]:text-xl [&>h1]:font-bold [&>h1]:text-gray-900 dark:[&>h1]:text-white">
      <div className="flex flex-1 flex-col px-6 pb-6">
        {!isEditing && <span className="absolute right-6 top-5 z-10 w-fit rounded-full bg-green-50 px-3 py-1 text-sm font-semibold capitalize text-green-700 dark:bg-green-500/10 dark:text-green-400">{entry.statut?.replace('_', ' ') || itemInfo.categorie}</span>}

        {itemInfo.image_url && (
          <div className="relative mb-5 aspect-[16/9] w-full shrink-0 overflow-hidden rounded-lg bg-gray-100 dark:bg-white/5 mt-4">
            <img src={itemInfo.image_url} alt={`Illustration`} className="absolute inset-0 h-full w-full object-cover" />
          </div>
        )}

        {isEditing ? (
          <div className="flex-1 flex flex-col mt-2 border-t border-gray-200 dark:border-white/10 pt-4">
            <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Statut</label>
            <select value={editStatut} onChange={(e) => setEditStatut(e.target.value as any)} className={inputStyle}>
              <option value="a_decouvrir">À découvrir</option><option value="en_cours">En cours</option><option value="termine">Terminé</option><option value="abandonne">Abandonné</option>
            </select>
            <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Note (/20)</label>
            <input type="number" min="0" max="20" value={editNote} onChange={(e) => setEditNote(e.target.value)} placeholder="Ex: 18" className={inputStyle} />
            <label className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Commentaire</label>
            <textarea value={editCommentaire} onChange={(e) => setEditCommentaire(e.target.value)} placeholder="Avis..." rows={3} className={`${inputStyle} resize-none`} />
            <div className="flex gap-2 mt-auto pt-4">
              <button onClick={handleSave} disabled={isSaving} className="flex-1 bg-green-500 hover:bg-green-600 text-white font-semibold py-2 rounded-lg transition">{isSaving ? 'Sauvegarde...' : 'Sauvegarder'}</button>
              <button onClick={() => setIsEditing(false)} disabled={isSaving} className="flex-1 bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-white font-semibold py-2 rounded-lg transition">Annuler</button>
            </div>
          </div>
        ) : (
          <>
            <p className="mb-5 flex-1 leading-relaxed text-gray-600 dark:text-gray-300">{itemInfo.description || 'Aucune description disponible.'}</p>
            <dl className="mb-6 grid grid-cols-2 gap-x-4 gap-y-3 border-t border-gray-200 pt-4 text-sm dark:border-white/10">
              <div><dt className="font-medium text-gray-500 dark:text-gray-400">Année</dt><dd className="mt-1 text-gray-900 dark:text-white">{itemInfo.annee || 'Inconnue'}</dd></div>
              <div><dt className="font-medium text-gray-500 dark:text-gray-400">Studio</dt><dd className="mt-1 text-gray-900 dark:text-white">{itemInfo.studio || 'Inconnu'}</dd></div>
            </dl>
            <div className="mt-auto border-t border-gray-200 pt-4 dark:border-white/10">
              {entry.note != null && <p className="text-sm font-semibold text-gray-900 dark:text-white mb-2">Note : <span className="text-green-500">{entry.note} / 20</span></p>}
              {entry.commentaire && <p className="text-sm italic text-gray-600 dark:text-gray-400 border-l-2 border-green-500 pl-3 mb-2">"{entry.commentaire}"</p>}
              <div className="flex justify-between items-center mt-4">
                <p className="text-xs text-gray-400">{entry.date && `Ajouté le ${new Date(entry.date).toLocaleDateString('fr-FR')}`}</p>
                <button onClick={() => setIsEditing(true)} className="text-xs font-semibold text-blue-500 hover:text-blue-600 dark:text-blue-400 dark:hover:text-blue-300 transition">Éditer l'avis</button>
              </div>
            </div>
          </>
        )}
      </div>
    </Card>
  );
}
