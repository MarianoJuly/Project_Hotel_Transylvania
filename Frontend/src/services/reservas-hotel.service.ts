import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { tap } from 'rxjs';
import { Hotel } from 'src/app/models/hotel';
import { PROXY_CONFIG } from 'src/proxy.conf';

@Injectable({
  providedIn: 'root'
})
export class ReservasHotelService {

  constructor(private httpClient: HttpClient){}

  hotelList(){
    return this.httpClient.get<Hotel[]>(`${PROXY_CONFIG.baseURlHotel}`)
    .pipe(
      tap(tipo => console.log(tipo))
    );
  }

  adicionaHotel(hotelNovo: any){
    return this.httpClient.post<any>(`${PROXY_CONFIG.baseURlHotel}`, hotelNovo);
  }

}
