from collections import defaultdict, deque
import heapq
from typing import Dict, List, Tuple, Optional

class Station:
    def __init__(self, idx: str, name: str, line: str):        
        self.idx = idx
        self.name = name
        self.line = line
        self.neighbors: List[Tuple["Station", int]] = [] # (Station, time) tuples

        # Parent station's index (for backtracking)
        self.parent_station = None
        # Total time to the station (g + h)
        self.f = float("inf")
        # Time from start to this station
        self.g = float("inf")
        # Heuristic time from this station to destination
        self.h = 0

    def add_neighbor(self, station: "Station", time: int):
        self.neighbors.append((station, time))

    def __lt__(self, other):
        # For priority queue to compare stations
        return self.idx < other.idx

    
class MetroNetwork:
    def __init__(self):
        self.stations: Dict[str, Station] = {}
        self.lines: Dict[str, List[Station]] = defaultdict(list)

    def add_station(self, idx: str, name: str, line: str) -> None:
        if idx not in self.stations:
            station = Station(idx, name, line)
            self.stations[idx] = station
            self.lines[line].append(station)

    def add_connection(self, station1_id: str, station2_id: str, time: int) -> None:
        station1 = self.stations[station1_id]
        station2 = self.stations[station2_id]
        station1.add_neighbor(station2, time)
        station2.add_neighbor(station1, time)

    def find_least_transfer(self, start_id: str, dest_id: str) -> Optional[List[Station]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """

        # TODO: Implement this function
        pass
        if start_id not in self.stations or dest_id not in self.stations:
            return None
        start_station = self.stations[start_id]
        dest_station = self.stations[dest_id]

        queue = deque([(start_station, [start_station])])
        visited = set()

        while queue:
            (current_station, path) = queue.popleft()

            # Mark the current station (node) as visited
            visited.add(current_station)

            # Check if destination is arrived
            if current_station == dest_station:
                return path
            
            # Explore neighbor stations
            for neighbor, travel_time in current_station.neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

            # Checking if neighbor_station is valid and not already visited
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

        # If no path is found, return None
        return None


    def find_fastest_route(self, start_id: str, dest_id: str) -> Optional[Tuple[List[Station], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur
        
        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın
        
        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
        """

        # TODO: Implement this function
        pass
        if start_id not in self.stations or dest_id not in self.stations:
            return None
        
        start_station = self.stations[start_id]
        dest_station = self.stations[dest_id]
        visited = set()

        # Reseting the f, g, and h values for the start station
        for station in self.stations.values():
            station.f = float("inf")
            station.g = float("inf")
            station.h = 0
            station.parent_station = None

        start_station.g = 0
        start_station.h = self.calculate_heuristic(start_station, dest_station)
        start_station.f = start_station.g + start_station.h

        open_list = [] # Priority queue for the A* (Star) Algo
        heapq.heappush(open_list, (start_station.f, start_station)) # including the start_station in the priority queue

        while open_list:
            f, current_station = heapq.heappop(open_list) # Extracting the station with the lowest f value from the priority queue
            visited.add(current_station) # Mark the current station as visited

            # Check if destination is reached and return the path
            if current_station == dest_station:
                path = self.trace_path(current_station)
                total_time = current_station.g
                return path, total_time

            for neighbor_station, travel_time in current_station.neighbors:
                if neighbor_station not in visited:
                    g_new = current_station.g + travel_time
                    h_new = self.calculate_heuristic(neighbor_station, dest_station)
                    f_new = g_new + h_new

                    if f_new < neighbor_station.f:
                        heapq.heappush(open_list, (f_new, neighbor_station))
                        neighbor_station.f = f_new
                        neighbor_station.g = g_new
                        neighbor_station.h = h_new
                        neighbor_station.parent_station = current_station
            
        # print(f"Checking station: {current_station.name}, f: {f}, g: {current_station.g}, h: {current_station.h}")

        # If no path is found, return None
        return None

    def trace_path(self, destination):
        """
        This function traces the path from destination station to the start station
        using the parent station information of each station. (Backtracking)

        Args:
            destination (Station): The destination station.

        Returns:
            List[Station]: The path from the destination station to the start station.
        """
        path = []
        current_station = destination

        while current_station is not None:
            path.append(current_station)
            current_station = current_station.parent_station # go back to the parent station
        
        path.reverse() # Reverse the path to get the path from start to destination

        return path
    
    def calculate_heuristic(self, current_station: "Station", dest_station: "Station") -> float:
        """
        This function calculates the heuristic time from the current station to the destination station.

        Args:
            current_station (Station): The current station.
            dest_station (Station): The destination station.

        Returns:
            float: The heuristic time from the current station to the destination station.
        """
        visited = set()
        queue = deque([(current_station, 0)]) # (station, accumulated_time)

        while queue:
            station, accumulated_time = queue.popleft()
            if station == dest_station:
                return accumulated_time
        
            visited.add(station)
            for neighbor_station, travel_time in station.neighbors:
                if neighbor_station not in visited:
                    queue.append((neighbor_station, accumulated_time + travel_time))
        
        # If destination cannot be reached
        return float("inf")


# Example Usage
if __name__ == "__main__":
    metro = MetroNetwork()

    # Add stations
    # Red Line
    metro.add_station("K1", "Kızılay", "Red Line")
    metro.add_station("K2", "Ulus", "Red Line")
    metro.add_station("K3", "Demetevler", "Red Line")
    metro.add_station("K4", "OSB", "Red Line")

    # Blue Line
    metro.add_station("M1", "AŞTİ", "Blue Line")
    metro.add_station("M2", "Kızılay", "Blue Line")
    metro.add_station("M3", "Sıhhiye", "Blue Line")
    metro.add_station("M4", "Gar", "Blue Line")

    # Orange Line
    metro.add_station("T1", "Batıkent", "Orange Line")
    metro.add_station("T2", "Demetevler", "Orange Line")
    metro.add_station("T3", "Gar", "Orange Line")
    metro.add_station("T4", "Keçiören", "Orange Line")

    # Add Connections
    # Red Line Connections
    metro.add_connection("K1", "K2", 4) # Kızılay -> Ulus
    metro.add_connection("K2", "K3", 6) # Ulus -> Demetevler
    metro.add_connection("K3", "K4", 8) # Demetevler -> OSB

    # Blue Line Connections
    metro.add_connection("M1", "M2", 5) # AŞTİ -> Kızılay
    metro.add_connection("M2", "M3", 3) # Kızılay -> Sıhhiye
    metro.add_connection("M3", "M4", 4) # Sıhhiye -> Gar

    # Orange Line Connections
    metro.add_connection("T1", "T2", 7) # Batıkent -> Demetevler
    metro.add_connection("T2", "T3", 9) # Demetevler -> Gar
    metro.add_connection("T3", "T4", 5) # Gar -> Keçiören

    # Line Transfer Connections (Same station different line)
    metro.add_connection("K1", "M2", 2) # Kızılay transfer
    metro.add_connection("K3", "T2", 3) # Demetevler transfer
    metro.add_connection("M4", "T3", 2) # Gar transfer

    # Test Scenarios
    print("\n=== Test Scenarios ===")

    # Scenario 1: From AŞTİ to OSB
    print("\n1. From AŞTİ to OSB: ")
    route = metro.find_least_transfer("M1", "K4")
    if route:
        print("Route with least transfers: ", " -> ".join(i.name for i in route))

    conclusion = metro.find_fastest_route("M1", "K4")
    if conclusion:
        route, time = conclusion
        print(f"Fastet route ({time} minutes): ", " -> ".join(i.name for i in route))
    
    # Scenario 2: From Batıkent to Keçiören
    print("\n2. From Batıkent to Keçiören: ")
    route = metro.find_least_transfer("T1", "T4")
    if route:
        print("Route with least transfers: ", " -> ".join(i.name for i in route))

    conclusion = metro.find_fastest_route("T1", "T4")
    if conclusion:
        route, time = conclusion
        print(f"Fastet route ({time} minutes): ", " -> ".join(i.name for i in route))
    
    # Scenario 1: From Keçiören to AŞTİ
    print("\n3. From Keçiören to AŞTİ: ")
    route = metro.find_least_transfer("T4", "M1")
    if route:
        print("Route with least transfers: ", " -> ".join(i.name for i in route))

    conclusion = metro.find_fastest_route("T4", "M1")
    if conclusion:
        route, time = conclusion
        print(f"Fastet route ({time} minutes): ", " -> ".join(i.name for i in route))

