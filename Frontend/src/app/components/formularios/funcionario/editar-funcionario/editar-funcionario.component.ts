import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

import { funcionario } from 'src/app/models/funcionario';
import { MessagesService } from 'src/services/messages.service';
import { ControleService } from 'src/services/controle.service';
import { ActivatedRoute, Router } from '@angular/router';
import { ControleFuncService } from 'src/services/controle-func.service';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-editar-funcionario',
  templateUrl: './editar-funcionario.component.html',
  styleUrls: ['./editar-funcionario.component.scss']
})
export class EditarFuncionarioComponent implements OnInit {
  
  
  async submit() {
      if(this.formulario.invalid){
        this.mensagens.add("Não foi possivel salvar o formulario");
        return;
      }else{
        this.controller.update(this.formulario.value).subscribe(result => {
          console.log(result);
          this.mensagens.add("Salvo com sucesso");
          this.rota.navigate(['home']);
          },
          error => {
            this.mensagens.add("Erro ao salvar o formulario" + error.error)
          }
        ); 
      }
      
  }
  
  
  constructor(private mensagens: MessagesService, private controller: ControleFuncService, private rota: Router, private route: ActivatedRoute)
  {
  } 
  
  ngOnInit(): void {
    this.route.params.subscribe(params => {
        this.cpf = params['cpf'];
    });
    this.controller.getData(this.cpf).subscribe((novoFuncionario: funcionario)=> {
    });
    this.formulario = new FormGroup({
        cpf: new FormControl(this.cpf),
        nome: new FormControl('', [Validators.required]),
        senha: new FormControl('', [Validators.required]),
    });
  }
  
@Output() onSubmit = new EventEmitter<funcionario>();
funcionario!: funcionario;

formulario!: FormGroup;

controle!: ControleService;

cpf!: string;


  async cancel() {
      this.mensagens.add("Inserção cancelada")
      this.rota.navigate(['home']);
  }


 get nome(){
   return this.formulario.get('nome')!;
 }

 get senha(){
  return this.formulario.get('senha')!;
 }

}
