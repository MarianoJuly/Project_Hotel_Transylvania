import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { faPenToSquare, faSearch, faTimes, faTrash } from '@fortawesome/free-solid-svg-icons';
import { catchError, of } from 'rxjs';
import { Hotel } from 'src/app/models/hotel';
import { ControleService } from 'src/services/controle.service';
import { MessagesService } from 'src/services/messages.service';
import { ReservasHotelService } from 'src/services/reservas-hotel.service';

@Component({
  selector: 'app-hotel-modal',
  templateUrl: './hotel-modal.component.html',
  styleUrls: ['./hotel-modal.component.scss']
})
export class HotelModalComponent {
    hoteis: Hotel[] = [];
    faSearch = faSearch; faTrash = faTrash; faTimes = faTimes; faPenToS = faPenToSquare;
    title = ''
    showMensage = false;

    constructor(private controla:ReservasHotelService,
                private mensage: MessagesService,
                private route: Router,
    ){
      this.controla.hotelList() //deveria estar no service
       .pipe(
        catchError(error => {
          this.mensage.add("Erro ao carregar");
          return of([])})
       )
       .subscribe(data => {
          this.hoteis = data
          this.showMe();
      });
    };

    ngOnInit(): void {
    };

    showMe(){
      if (this.hoteis.length === 0) {
        this.title= 'Não há dados salvos.';
      } else {
        this.title = 'Os dados são: ';
      }
      this.showMensage = true;
    }

    displayColumns = ['ID', 'Name','Quantidade de quartos', 'Localização', 'Funções']
}
