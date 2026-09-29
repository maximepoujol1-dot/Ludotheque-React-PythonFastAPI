export async function getItems() {
  const reponse = await fetch("http://localhost:8000/items")
  const donnees = await reponse.json()
  return donnees
}
