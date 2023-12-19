import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

import { DataClient } from '../../../models/dataClient';
import { MessagesService } from 'src/services/messages.service';
import { ControleService } from 'src/services/controle.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-first-component',
  templateUrl: './first-component.component.html',
  styleUrls: ['./first-component.component.scss']
})

export class FirstComponentComponent implements OnInit{

@Output() onSubmit = new EventEmitter<DataClient>();
dataClient!: DataClient;

formulario!: FormGroup;

controle!: ControleService;

test!: string;


async submit() {
    if(this.formulario.invalid){
      this.mensagens.add("Não foi possivel salvar o formulario");
      return;
    }else{
      this.controller.create(this.formulario.value).subscribe(resul => console.log(resul));
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

  constructor(
              private mensagens: MessagesService,
              private controller: ControleService,
              private rota: Router
              ){};

  ngOnInit(): void {
      this.formulario = new FormGroup({
        name: new FormControl('', [Validators.required]),
        idade: new FormControl('', [Validators.required]),
      });
 }

 get name(){
   return this.formulario.get('name')!;
 }

 get idade(){
   return this.formulario.get('idade')!;
 }

}
