class Solution {
private:
    int five = 0, ten = 0;
public:
    bool lemonadeChange(vector<int>& bills) {
        for (int bill: bills){
            if (bill==5) five++;
            if (bill==10){
                if (five == 0) return false;
                five--; ten++;
            }
            if (bill==20){
                if (five>0 && ten >0){
                    five--; ten--;
                } else if (five>2){
                    five-=3;
                } else {return false;}
            }
        }
        return true;
    }
};