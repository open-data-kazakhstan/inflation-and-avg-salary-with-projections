from datapackage import Package

package = Package()
package.infer('archive/csv_wranged.csv')
package.infer('data/csv_expanded2.csv')
package.infer('data/prediction.csv')
package.commit()
package.save('datapackage.json')