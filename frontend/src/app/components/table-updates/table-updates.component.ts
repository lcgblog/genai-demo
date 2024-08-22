import { Component, OnInit } from '@angular/core';
import { WebSocketService } from '../../services/web-socket.service';

@Component({
  selector: 'app-table-updates',
  templateUrl: './table-updates.component.html',
  styleUrls: ['./table-updates.component.css']
})
export class TableUpdatesComponent implements OnInit {
  tableData: any[] = [];
  displayedColumns: string[] = ['key', 'cusip', 'account', 'netposition', 'price'];

  constructor(private webSocketService: WebSocketService) {}

  ngOnInit(): void {
    this.webSocketService.getPositions('mockUser', data => {
      this.tableData = data;
    });
  }

  addPosition(): void {
    this.webSocketService.addPosition({key:"123"})
  }
}