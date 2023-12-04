import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ModalComponent } from './components/modal/modal.component';
import { MensagemComponent } from './components/mensagem/mensagem.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { RouterLink } from '@angular/router';
import { CabecalhoComponent } from './components/cabecalho/cabecalho.component';
import { HomeComponent } from './components/home/home.component';
import { RegistrarFuncionariosComponent } from './components/formularios/registrar-funcionarios/registrar-funcionarios.component';
import { RegistrarHotelComponent } from './components/formularios/registrar-hotel/registrar-hotel.component';
import { FirstComponentComponent } from './components/formularios/registrar-cliente/first-component.component';


@NgModule({
  declarations: [
    AppComponent,
    ModalComponent,
    MensagemComponent,
    FirstComponentComponent,
    CabecalhoComponent,
    HomeComponent,
    RegistrarFuncionariosComponent,
    RegistrarHotelComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    FontAwesomeModule,
    RouterLink,
  ],
  providers: [],
  bootstrap: [AppComponent,ModalComponent,MensagemComponent]
})
export class AppModule { }
