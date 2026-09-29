import type { Game } from './types/type'

export const getItems = async (page: number) => {
  const response = await fetch(`http://localhost:8000/items?page=${page}`)
  return response.json()
}
