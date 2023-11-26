import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetalheHotelComponent } from './detalhe-hotel.component';

describe('DetalheHotelComponent', () => {
  let component: DetalheHotelComponent;
  let fixture: ComponentFixture<DetalheHotelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DetalheHotelComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DetalheHotelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
