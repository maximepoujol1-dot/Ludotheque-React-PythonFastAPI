import { requete } from './httpClient'

export const getItems = async (page: number) => {
  return await requete(`/items?page=${page}`)
}
