const BASE_URL = "http://localhost:8000"

export const requete = async (endpoint: string, options: RequestInit = {}) => {
  const response = await fetch(`${BASE_URL}${endpoint}`, options)
  return response.json()
}
