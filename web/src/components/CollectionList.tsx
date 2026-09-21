import React from 'react'
import type { Game } from '../types/type'
import GameCollectionCard from './CollectionCard'

interface CollectionListProps {
	games: Game[]
}

const CollectionList = ({ games }: CollectionListProps) => {

	if (games.length === 0) {
		return <p>Aucune collection</p>
	}

	return (
		<ul>
			{games.map((game) => (
				<li key={game.id}>
					<GameCollectionCard game={game} />
				</li>
			))}
		</ul>
	)
}

export default CollectionList
