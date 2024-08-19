import { NgModule } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatTableModule } from '@angular/material/table';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppComponent } from './app.component';
import { TableUpdatesComponent } from './components/table-updates/table-updates.component';

@NgModule({
  declarations: [
    AppComponent,
    TableUpdatesComponent
  ],
  imports: [
    BrowserModule,
    MatTableModule,
    MatButtonModule,
    BrowserAnimationsModule,
    // other imports
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }