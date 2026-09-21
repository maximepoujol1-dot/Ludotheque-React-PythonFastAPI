import React from 'react'
import type { Game } from '../types/type'

interface CatalogueCardProps {
	game: Game
}

const CatalogueCard = ({ game }: CatalogueCardProps) => {
  return (
	<div>
		<h3>{game.title}</h3>
		<p>{game.description ?? 'Aucune description'}</p>
	</div>
  )
}

export default CatalogueCard