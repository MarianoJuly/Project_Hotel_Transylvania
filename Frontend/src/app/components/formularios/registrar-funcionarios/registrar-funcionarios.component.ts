import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ListService } from '../../../../services/list.service';

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

  constructor(private listService: ListService,
              private mensagens: MessagesService,
              private controller: ControleFuncService,
              private rota: Router
              ){};

  ngOnInit(): void {
      this.formulario = new FormGroup({
        name: new FormControl('', [Validators.required]),
        cpfClient: new FormControl('', [Validators.required]),
        senha: new FormControl('', [Validators.required]),
      });
 }

 get name(){
   return this.formulario.get('name')!;
 }

 get cpfClient(){
   return this.formulario.get('cpfClient')!;
 }

 get senha(){
  return this.formulario.get('senha')!;
 }

}
