import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { Hotel } from 'src/app/models/hotel';
import { ControleService } from 'src/services/controle.service';
import { MessagesService } from 'src/services/messages.service';
import { ReservasHotelService } from 'src/services/reservas-hotel.service';

@Component({
  selector: 'app-registrar-hotel',
  templateUrl: './registrar-hotel.component.html',
  styleUrls: ['./registrar-hotel.component.scss']
})
export class RegistrarHotelComponent {
  
  formulario!: FormGroup;

  constructor(private mensagens: MessagesService,
    private controller: ReservasHotelService,
    private rota: Router
    ){};


async submit() {
    if(this.formulario.invalid){
      this.mensagens.add("Não foi possivel salvar o formulario");
      return;
    }else{
      this.controller.adicionaHotel(this.formulario.value).subscribe(resul => console.log(resul));
      this.mensagens.add("Formulario Salvo com sucesso");
      this.resetForm();
      this.rota.navigate(['home']);
    }
  }

  async resetForm(){
    this.formulario.reset();
  }

  async cancel() {
      this.resetForm();
      this.mensagens.add("Inserção cancelada")
      this.rota.navigate(['home']);
  }

  ngOnInit(): void {
      this.formulario = new FormGroup({
        nome: new FormControl('', [Validators.required]),
        localizacao: new FormControl('', [Validators.required]),
      });
 }

 get nome(){
   return this.formulario.get('nome')!;
 }

 get localizacao(){
  return this.formulario.get('localizacao')!;
 }


}
