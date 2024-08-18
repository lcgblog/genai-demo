package com.citi.onepx.genaidemo.demo.controller;

import java.util.List;
import java.util.Map;

import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.stereotype.Controller;

import com.citi.onepx.genaidemo.demo.domain.Position;
import com.citi.onepx.genaidemo.demo.service.TableService;

import lombok.RequiredArgsConstructor;
import reactor.core.publisher.Flux;

@Controller
@RequiredArgsConstructor
public class WebSocketController {

	private final TableService tableService;

	@MessageMapping("/getFullPosition")
	@SendTo("/topic/fullPosition")
	public List<Position> getFullPosition() {
        tableService.clearTable();
        tableService.addPosition(new Position("1","AAPL", "Apple Inc.", 100.0, 150.25));
        tableService.addPosition(new Position("2", "GOOGL", "Alphabet Inc.", 50.0, 2500.75));
        tableService.addPosition(new Position("3", "MSFT", "Microsoft Corporation", 75.0, 300.50));
		return tableService.getTableData();
	}

	@MessageMapping("/getPositionUpdates")
	@SendTo("/topic/positionUpdates")
	public Flux<Map<String, Position>> getPositionUpdates() {
		return tableService.getTableUpdates();
	}

}