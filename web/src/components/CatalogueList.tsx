import React from 'react'
import GameCatalogueCard from './CatalogueCard'
import type { Game } from '../types/type'

interface GameListProps {
	games: Game[] 
}

const GameList = ({ games,}: GameListProps) => {

	if (games.length === 0) {
		return <p>Aucun jeu</p>
	}

	return (
		<ul>
			{games.map((game) => (
				<li key={game.id}>
					<GameCatalogueCard game={game} />
				</li>
			))}
		</ul>
	)
}

export default GameList
