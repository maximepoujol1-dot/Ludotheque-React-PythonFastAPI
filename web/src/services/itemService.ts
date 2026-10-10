import { requete } from './httpClient'

export const getItems = async (q: string | null, page: number, categorie: string | null) => {
  if (q && categorie){
    return await requete(`/items?q=${q}&page=${page}&categorie=${categorie}`)
  } else if (q){
    return await requete(`/items?q=${q}&page=${page}`)
  } else if (categorie){
    return await requete(`/items?page=${page}&categorie=${categorie}`)
  }
  
  return await requete(`/items?page=${page}`)
}
