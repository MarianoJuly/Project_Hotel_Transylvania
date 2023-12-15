import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';

import { funcionario } from 'src/app/models/funcionario';
import { MessagesService } from 'src/services/messages.service';
import { ControleService } from 'src/services/controle.service';
import { ActivatedRoute, Router } from '@angular/router';
import { ControleFuncService } from 'src/services/controle-func.service';


@Component({
  selector: 'app-editar-funcionario',
  templateUrl: './editar-funcionario.component.html',
  styleUrls: ['./editar-funcionario.component.scss']
})
export class EditarFuncionarioComponent implements OnInit {

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
        this.controller.create(this.formulario.value).subscribe(result => {
          console.log(result);
          this.mensagens.add("Formulário salvo com sucesso");
          this.resetForm();
          this.rota.navigate(['home']);
          },
          error => {
            this.mensagens.add("Erro ao salvar o formulario" + error.error)
          }
        ); 
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
                private rota: Router,
                private route: ActivatedRoute
                ){};
  
    ngOnInit(): void {
      const idFuncionario = this.route.snapshot.paramMap.get('cpf');
      this.controller.getData(idFuncionario!).subscribe((funcionario) => {
        this.formulario = new FormGroup({
          cpf: new FormControl(funcionario.cpf, [Validators.required]),
          nome: new FormControl(funcionario.nome, [Validators.required]),
          senha: new FormControl(funcionario.senha, [Validators.required]),
        });
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
  