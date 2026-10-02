export type Statut = "a_decouvrir" | "en_cours" | "termine";

export interface Game {
  id: number
  titre: string
  categorie: "fps" | "rpg" | "rts" | "gestion"
  description: string
  image_url: string
  annee: number
  studio: string
  directeur: string
}
