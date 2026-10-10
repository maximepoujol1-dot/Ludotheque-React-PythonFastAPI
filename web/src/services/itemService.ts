import { requete } from './httpClient'

export const getItems = async (page: number, categorie: string | null) => {
  if (categorie){
    return await requete(`/items?page=${page}&categorie=${categorie}`)
  }
  
  return await requete(`/items?page=${page}`)
}
