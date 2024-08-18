import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TableUpdatesComponent } from './table-updates.component';

describe('TableUpdatesComponent', () => {
  let component: TableUpdatesComponent;
  let fixture: ComponentFixture<TableUpdatesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TableUpdatesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TableUpdatesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
