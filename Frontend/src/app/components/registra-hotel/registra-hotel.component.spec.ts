import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistraHotelComponent } from './registra-hotel.component';

describe('RegistraHotelComponent', () => {
  let component: RegistraHotelComponent;
  let fixture: ComponentFixture<RegistraHotelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RegistraHotelComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RegistraHotelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
