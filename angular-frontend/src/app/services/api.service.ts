import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Notebook } from '../models';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:3000/api'; // Adjust the URL as needed

  constructor(private http: HttpClient) {}

  getNotebooks(): Observable<Notebook[]> {
    return this.http.get<Notebook[]>(`${this.apiUrl}/notebooks`);
  }

  saveNotebook(notebook: Notebook): Observable<Notebook> {
    return this.http.post<Notebook>(`${this.apiUrl}/notebooks`, notebook);
  }
}