import { HttpClient } from '@angular/common/http';
import { Injectable, Input } from '@angular/core';
import { BehaviorSubject, Observable, catchError, tap, throwError } from 'rxjs';
import { funcionario } from 'src/app/models/funcionario';
import { PROXY_CONFIG } from 'src/proxy.conf';

@Injectable({
  providedIn: 'root'
})
export class ControleFuncService {

    constructor(private httpClient: HttpClient) {}

    list(){
      return this.httpClient.get<funcionario[]>(`${PROXY_CONFIG.baseURlFUNC}`)
      .pipe(
        tap(tipo => console.log(tipo))
      );
    }

    create(newData: funcionario){
      return this.httpClient.post<funcionario>(`${PROXY_CONFIG.baseURlFUNC}`, newData);
    }


    update(alterData: funcionario){
      return this.httpClient.put<funcionario>(`${PROXY_CONFIG.baseURlFUNC}/edit/${alterData.idFuncionario}`, alterData);
    }

    deletaTudo(idFunc: string){
      return this.httpClient.delete(`${PROXY_CONFIG.baseURlFUNC}/${idFunc}`)
      .pipe(
        tap(response => console.log(response)),
          catchError(error => {
            console.error(error);
            return throwError('Erro ao excluir objeto');
          })
        );
    }

    getData(idFunc: string){
      return this.httpClient.get<funcionario>(`${PROXY_CONFIG.baseURlFUNC}/${idFunc}`);
    }

    searsh(input: string){
      return this.httpClient.get<funcionario[]>(`${PROXY_CONFIG.baseURlFUNC}/${input}`);
    }

  }
