import React, { createContext, useContext, useState, ReactNode } from 'react';

export type Status = 'a_decouvrir' | 'a_faire' | 'en_cours' | 'termine' | 'abandonne';

export interface Item {
  id: number;
  titre: string;
  categorie: string;
  description: string;
  image_url: string;
  annee: number;
  studio: string;
  directeur: string;
}

export interface CollectionEntry {
  id: number;
  item: Item;
  statut: Status;
  date: string;
  note?: number;
  commentaire?: string;
}

interface CollectionContextType {
  collection: CollectionEntry[];
  setCollection: (items: CollectionEntry[]) => void;
  addEntry: (entry: CollectionEntry) => void;
  updateEntry: (entryId: number, updatedEntry: CollectionEntry) => void;
  removeEntry: (entryId: number) => void;
}

const CollectionContext = createContext<CollectionContextType | undefined>(undefined);

export const CollectionProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [collection, setCollectionState] = useState<CollectionEntry[]>([]);

  const setCollection = (items: CollectionEntry[]) => setCollectionState(items);

  const addEntry = (entry: CollectionEntry) => {
    setCollectionState((prev) => {
      if (prev.some((e) => e.id === entry.id)) return prev;
      return [...prev, entry];
    });
  };

  const updateEntry = (entryId: number, updatedEntry: CollectionEntry) => {
    setCollectionState((prev) =>
      prev.map((entry) => (entry.id === entryId ? updatedEntry : entry))
    );
  };

  const removeEntry = (entryId: number) => {
    setCollectionState((prev) => prev.filter((entry) => entry.id !== entryId));
  };

  return (
    <CollectionContext.Provider value={{ collection, setCollection, addEntry, updateEntry, removeEntry }}>
      {children}
    </CollectionContext.Provider>
  );
};

export const useCollection = () => {
  const context = useContext(CollectionContext);
  if (!context) throw new Error("useCollection doit être dans CollectionProvider");
  return context;
};
