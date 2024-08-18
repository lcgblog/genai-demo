package com.citi.onepx.genaidemo.demo.service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Service;

import com.citi.onepx.genaidemo.demo.domain.Position;

import reactor.core.publisher.Flux;
import reactor.core.publisher.Sinks;

@Service
public class TableService {
	private final Map<String, Position> tableData = new HashMap<>();
	private final Sinks.Many<Map<String, Position>> sink = Sinks.many().multicast().onBackpressureBuffer();

	public Flux<Map<String, Position>> getTableUpdates() {
		return sink.asFlux();
	}

	public void updateTable(List<Position> newTableData) {
		tableData.clear();
		for (Position position : newTableData) {
			tableData.put(position.getKey(), position);
		}
		sink.tryEmitNext(new HashMap<>(tableData));
	}

	public List<Position> getTableData() {
		return new ArrayList<>(tableData.values());
	}

	public void clearTable() {
		tableData.clear();
		sink.tryEmitNext(new HashMap<>(tableData));
	}

	public void addPosition(Position position) {
		tableData.put(position.getKey(), position);
		sink.tryEmitNext(new HashMap<>(tableData));
	}

	public void deletePosition(String key) {
		tableData.remove(key);
		sink.tryEmitNext(new HashMap<>(tableData));
	}
}
