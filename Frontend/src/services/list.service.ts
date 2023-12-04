import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ListService {

  constructor(private http: HttpClient) {}

  async getAddress(cep: string ): Promise<Observable<String[]>>{
    // toggleLoader();
   return this.http.get<String[]>(`https://viacep.com.br/ws/${cep}/json/`);
  };
}
