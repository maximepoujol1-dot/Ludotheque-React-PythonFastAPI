import React from 'react'
import type { Game } from '../types/type'

interface CollectionCardProps {
	game: Game
}

const CollectionCard = ({ game }: CollectionCardProps) => {
	return (
		<div>
			<h3>{game.title}</h3>
			<p>{game.description ?? 'Aucune description'}</p>
		</div>
	)
}

export default CollectionCard
