import { MatTableModule } from '@angular/material/table';
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
import { LoginComponent } from './components/formularios/login/login.component';
import { HotelModalComponent } from './components/hotel-modal/hotel-modal.component';
import { RegistrarReservaComponent } from './components/formularios/registrar-reserva/registrar-reserva.component';
import { ReservaModalComponent } from './components/reserva-modal/reserva-modal.component';


@NgModule({
  declarations: [
    AppComponent,
    ModalComponent,
    MensagemComponent,
    FirstComponentComponent,
    LoginComponent,
    CabecalhoComponent,
    HomeComponent,
    RegistrarFuncionariosComponent,
    RegistrarHotelComponent,
    HotelModalComponent,
    RegistrarReservaComponent,
    ReservaModalComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    FontAwesomeModule,
    RouterLink,
    MatTableModule
  ],
  providers: [],
  bootstrap: [AppComponent,ModalComponent,MensagemComponent]
})
export class AppModule { }
