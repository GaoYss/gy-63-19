import { http } from './http'

export const levelApi = {
  list: () => http.get('/levels'),
  create: (payload) => http.post('/levels', payload),
  update: (id, payload) => http.patch(`/levels/${id}`, payload),
}
