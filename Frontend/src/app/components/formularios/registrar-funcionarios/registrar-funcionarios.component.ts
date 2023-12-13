import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

import { funcionario } from 'src/app/models/funcionario';
import { MessagesService } from 'src/services/messages.service';
import { ControleService } from 'src/services/controle.service';
import { Router } from '@angular/router';
import { ControleFuncService } from 'src/services/controle-func.service';


@Component({
  selector: 'app-registrar-funcionarios',
  templateUrl: './registrar-funcionarios.component.html',
  styleUrls: ['./registrar-funcionarios.component.scss']
})

export class RegistrarFuncionariosComponent implements OnInit {

@Output() onSubmit = new EventEmitter<funcionario>();
funcionario!: funcionario;

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

  constructor(private mensagens: MessagesService,
              private controller: ControleFuncService,
              private rota: Router
              ){};

  ngOnInit(): void {
      this.formulario = new FormGroup({
        cpf: new FormControl("", [Validators.required]),
        nome: new FormControl("", [Validators.required]),
        senha: new FormControl("", [Validators.required]),
      });
 }

 get nome(){
   return this.formulario.get('nome')!;
 }

 get cpf(){
   return this.formulario.get('cpf')!;
 }

 get senha(){
  return this.formulario.get('senha')!;
 }

}
