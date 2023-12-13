import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { MessagesService } from 'src/services/messages.service';

@Component({
  selector: 'app-registrar-reserva',
  templateUrl: './registrar-reserva.component.html',
  styleUrls: ['./registrar-reserva.component.scss']
})
export class RegistrarReservaComponent implements OnInit{
  formulario!: FormGroup;
  
  ngOnInit(): void {
    this.formulario = new FormGroup({
      id_cliente: new FormControl("", [Validators.required]),
      id_quarto: new FormControl("", [Validators.required]),
      dataEntrada: new FormControl("", [Validators.required]),
      dataSaida: new FormControl("", [Validators.required]),
    });
  }

  constructor(private mensagens: MessagesService,
    private rota: Router
    ){};



  async submit() {
    if(this.formulario.invalid){
      this.mensagens.add("Não foi possivel salvar o formulario");
      return;
    }else{
      // this.controller.adicionaHotel(this.formulario.value).subscribe(resul => console.log(resul));
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

  get id_cliente(){
    return this.formulario.get('id_cliente')!;
  }
 
  get id_quarto(){
    return this.formulario.get('id_quarto')!;
  }
 
  get dataEntrada(){
   return this.formulario.get('dataEntrada')!;
  }

  get dataSaida(){
    return this.formulario.get('dataSaida')
  }
}
