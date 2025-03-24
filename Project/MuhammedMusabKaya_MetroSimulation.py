from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Station:
    def __init__(self, idx: str, name: str, line: str):
        self.idx = idx
        self.name = name
        self.line = line
        self.neighbors: List[Tuple["Station", int]] = [] # (Station, time) tuples

    def add_neighbor(self, station: "Station", time: int):
        self.neighbors.append((station, time))

    
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
        visited = Set()

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
        visited = Set()

        # # Parent cell's row index
        # self.parent_station = 0
        # # Parent cell's column index
        # # Total cost of the cell (g + h)
        # self.f = float("inf")
        # # Cost from start to this cell
        # self.g = float("inf")
        # # Heuristic cost from this cell to destination
        # self.h = 0

        # # Check if a cell is valid (within the grid 
        # return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

        # # Check if a cell is the destination
        # return row == dest[0] and col == dest[1]

        # # Calculate the heuristic value of a cell (Euclidean distance to destination)
        # return ((row - dest[0]) ** 2 + (col - dest[1]) ** 2) ** 0.5

        # print("The path is ")
        # path = []
        # row = dest[0]
        # col = dest[1]

        # # Trace the path from destination to source using parent cells
        # while not (cell_details[row][col].parent_i == row and
        #         cell_details[row][col].parent_j == col):
        #     path.append((row, col))
        #     temp_row = cell_details[row][col].parent_i
        #     temp_col = cell_details[row][col].parent_j
        #     row = temp_row
        #     col = temp_col

        # # Add the source cell to the path
        # path.append((row, col))
        
        # # Reverse the path to get the path from source to destination
        # path.reverse()

        # # Print the path
        # for i in path:
        #     print("->", i, end=" ")
        # print()

        def a_star_search(grid, src, dest):
            # Check if the source and destination are valid
            if not is_valid(src[0], src[1]) or not is_valid(dest[0], dest[1]):
                print("Source or destination is invalid")
                return
            
            # Check if the source and destination are unblocked
            if not is_unblocked(grid, src[0], src[1] or not is_unblocked(grid, dest[0], dest[1])):
                print("Source or destination is blocked")
                return
            
            # Check if we are already at the destination
            if is_destination(src[0], src[1], dest):
                print("We are already at he destination")
                return
            
            # Initialize the closed list (visited cells)
            closed_list = [[False for _ in range(COL)] for _ in range(ROW)]

            # Initialize the details of each cell
            cell_details = [[Cell() for _ in range(COL)] for _ in range(ROW)]

            # Initialize the start cell details
            i = src[0]
            j = src[1]
            cell_details[i][j].f = 0
            cell_details[i][j].g= 0
            cell_details[i][j].h = 0
            cell_details[i][j].parent_i = i
            cell_details[i][j].parent_j = j

            # Initialize the open list (cells to be visited) with the start cell
            open_list = []
            heapq.heappush(open_list, (0.0, i, j))

            # Initialize the flag for whether destination is found
            found_dest = False

            # Main loop of the A* (Star) Search Algorithm
            while len(open_list) > 0:
                # Pop the cell with the lowest f value from the open list
                p = heapq.heappop(open_list)

                # Mark the cell as visited
                i = p[1]
                j = p[2]
                closed_list[i][j] = True

                # For each direction, check the successors
                directions = [(0, -1), (0, 1), (1, 0), (-1, 0),
                            (1, 1), (1, -1), (-1, 1), (-1, -1)]
                
                for dir in directions:
                    new_i = i + dir[0]
                    new_j = j + dir[1]

                    # If the successor is valid, unblocked, and not visited
                    if is_valid(new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                        # If the successoris the destination
                        if is_destination(new_i, new_j, dest):
                            # Set the parent of the destination cell
                            cell_details[new_i][new_j].parent_i = i
                            cell_details[new_i][new_j].parent_j = j
                            print("The destination cell is found")

                            #Trace and print the path from source to destination
                            trace_path(cell_details, dest)
                            found_dest = True
                            return
                    else:
                        # Calculate the new f, g, and h values
                        g_new = cell_details[i][j].g + 1.0
                        h_new = calculate_h_value(new_i, new_j, dest)
                        f_new = g_new + h_new

                        # If the cell is not in the open list or the new f value is smaller
                        if cell_details[new_i][new_j].f == float("inf") or cell_details[new_i][new_j].f > f_new:
                            
                            # Add the cell to the open list
                            heapq.heappush(open_list, (f_new, new_i, new_j))

                            # Update the cell details
                            cell_details[new_i][new_j].f = f_new
                            cell_details[new_i][new_j].g = g_new
                            cell_details[new_i][new_j].h = h_new
                            cell_details[new_i][new_j].parent_i = i
                            cell_details[new_i][new_j].parent_j = j

            # If the destination is not found after visiting all cells
            if not found_dest:
                print("Failed to find the destination cell")


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
    print("\n=== Test Scenarios===")

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
    print("\n1. From Batıkent to Keçiören: ")
    route = metro.find_least_transfer("T1", "T4")
    if route:
        print("Route with least transfers: ", " -> ".join(i.name for i in route))

    conclusion = metro.find_fastest_route("T1", "T4")
    if conclusion:
        route, time = conclusion
        print(f"Fastet route ({time} minutes): ", " -> ".join(i.name for i in route))
    
    # Scenario 1: From Keçiören to AŞTİ
    print("\n1. From Keçiören to AŞTİ: ")
    route = metro.find_least_transfer("T4", "M1")
    if route:
        print("Route with least transfers: ", " -> ".join(i.name for i in route))

    conclusion = metro.find_fastest_route("T4", "M1")
    if conclusion:
        route, time = conclusion
        print(f"Fastet route ({time} minutes): ", " -> ".join(i.name for i in route))

