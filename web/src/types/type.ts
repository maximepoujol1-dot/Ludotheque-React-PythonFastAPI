export type Statut = "a_decouvrir" | "en_cours" | "termine";

export interface Game {
	id: number;
	title: string;
	description: string;
	status: Statut;
	note: number;
}